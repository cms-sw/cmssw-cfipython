import FWCore.ParameterSet.Config as cms

def DTRecoIdealDBLoader(*args, **kwargs):
  mod = cms.EDAnalyzer('DTRecoIdealDBLoader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
