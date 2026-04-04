import FWCore.ParameterSet.Config as cms

def TrackingRecoMaterialAnalyser(*args, **kwargs):
  mod = cms.EDProducer('TrackingRecoMaterialAnalyser',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
