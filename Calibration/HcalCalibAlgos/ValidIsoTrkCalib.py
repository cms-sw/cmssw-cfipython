import FWCore.ParameterSet.Config as cms

def ValidIsoTrkCalib(**kwargs):
  mod = cms.EDAnalyzer('ValidIsoTrkCalib',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
