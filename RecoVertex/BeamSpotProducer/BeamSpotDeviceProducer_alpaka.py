import FWCore.ParameterSet.Config as cms

def BeamSpotDeviceProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('BeamSpotDeviceProducer@alpaka',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
