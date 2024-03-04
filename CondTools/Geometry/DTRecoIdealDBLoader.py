import FWCore.ParameterSet.Config as cms

def DTRecoIdealDBLoader(**kwargs):
  mod = cms.EDAnalyzer('DTRecoIdealDBLoader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
