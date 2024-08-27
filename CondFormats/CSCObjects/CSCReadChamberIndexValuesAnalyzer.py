import FWCore.ParameterSet.Config as cms

def CSCReadChamberIndexValuesAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCReadChamberIndexValuesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
