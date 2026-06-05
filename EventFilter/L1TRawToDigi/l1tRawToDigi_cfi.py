import FWCore.ParameterSet.Config as cms

from .L1TRawToDigi import L1TRawToDigi

l1tRawToDigi = L1TRawToDigi(

  FWId = 1,
  FedIds = [1352],
  InputLabel = ('l1tDigiToRaw'),
  Setup = 'stage2::CaloSetup'
)
