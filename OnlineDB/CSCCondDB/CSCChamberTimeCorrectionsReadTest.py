import FWCore.ParameterSet.Config as cms

def CSCChamberTimeCorrectionsReadTest(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCChamberTimeCorrectionsReadTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
