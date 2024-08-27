import FWCore.ParameterSet.Config as cms

def CSCReadChamberTimeCorrAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCReadChamberTimeCorrAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
