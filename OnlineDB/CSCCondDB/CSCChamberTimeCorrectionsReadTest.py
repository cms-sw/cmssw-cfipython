import FWCore.ParameterSet.Config as cms

def CSCChamberTimeCorrectionsReadTest(**kwargs):
  mod = cms.EDAnalyzer('CSCChamberTimeCorrectionsReadTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
