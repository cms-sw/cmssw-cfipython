import FWCore.ParameterSet.Config as cms

from .L1TRawToDigi import L1TRawToDigi

l1tRawToDigi = L1TRawToDigi(
  FedIds = [1352],
  Setup = 'stage2::CaloSetup',
  FWId = 1,
  DmxFWId = 0,
  FWOverride = False,
  TMTCheck = True,
  CTP7 = False,
  MTF7 = False,
  InputLabel = ('l1tDigiToRaw'),
  lenSlinkHeader = 8,
  lenSlinkTrailer = 8,
  lenAMCHeader = 8,
  lenAMCTrailer = 0,
  lenAMC13Header = 8,
  lenAMC13Trailer = 8,
  debug = False,
  MinFeds = 0
)
