import FWCore.ParameterSet.Config as cms

def CandIsoComparer(**kwargs):
  mod = cms.EDAnalyzer('CandIsoComparer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
