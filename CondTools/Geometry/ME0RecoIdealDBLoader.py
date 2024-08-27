import FWCore.ParameterSet.Config as cms

def ME0RecoIdealDBLoader(**kwargs):
  mod = cms.EDAnalyzer('ME0RecoIdealDBLoader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
