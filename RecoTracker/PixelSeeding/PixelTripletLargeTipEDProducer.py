import FWCore.ParameterSet.Config as cms

def PixelTripletLargeTipEDProducer(*args, **kwargs):
  mod = cms.EDProducer('PixelTripletLargeTipEDProducer',
    doublets = cms.InputTag('hitPairEDProducer'),
    produceSeedingHitSets = cms.bool(False),
    produceIntermediateHitTriplets = cms.bool(False),
    maxElement = cms.uint32(1000000),
    extraHitRPhitolerance = cms.double(0),
    extraHitRZtolerance = cms.double(0),
    useMultScattering = cms.bool(True),
    useBending = cms.bool(True),
    useFixedPreFiltering = cms.bool(False),
    phiPreFiltering = cms.double(0.3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
