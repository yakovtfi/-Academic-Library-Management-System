class SystemAdmin:
    total_transactions: int = 0

    @classmethod
    def update_transactions_count(cls, amount: int = 1) -> None:
        cls.total_transactions += amount

    @classmethod
    def report_stats(cls) -> None:
        from models1.library import Library
        print("\n_____ System Statistics______")
        print(f"Total Transactions: {cls.total_transactions}")
        print(f"Max Borrow Days: {Library.max_borrow_days}")