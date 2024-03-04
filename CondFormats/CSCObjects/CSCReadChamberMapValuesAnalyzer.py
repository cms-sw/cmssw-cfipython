import FWCore.ParameterSet.Config as cms

def CSCReadChamberMapValuesAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCReadChamberMapValuesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
