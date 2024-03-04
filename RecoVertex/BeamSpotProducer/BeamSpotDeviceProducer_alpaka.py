import FWCore.ParameterSet.Config as cms

def BeamSpotDeviceProducer_alpaka(**kwargs):
  mod = cms.EDProducer('BeamSpotDeviceProducer@alpaka',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
