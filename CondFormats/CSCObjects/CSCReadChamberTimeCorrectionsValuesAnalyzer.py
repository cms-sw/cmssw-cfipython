import FWCore.ParameterSet.Config as cms

def CSCReadChamberTimeCorrectionsValuesAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCReadChamberTimeCorrectionsValuesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
