import FWCore.ParameterSet.Config as cms

def MTDDigiDump(**kwargs):
  mod = cms.EDAnalyzer('MTDDigiDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
