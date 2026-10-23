import FWCore.ParameterSet.Config as cms

def CSCReadChamberTimeCorrectionsValuesAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCReadChamberTimeCorrectionsValuesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
