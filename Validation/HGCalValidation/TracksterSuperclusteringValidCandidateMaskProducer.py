import FWCore.ParameterSet.Config as cms

def TracksterSuperclusteringValidCandidateMaskProducer(*args, **kwargs):
  mod = cms.EDProducer('TracksterSuperclusteringValidCandidateMaskProducer',
    tracksters = cms.required.InputTag,
    associatorRecoToSim = cms.required.InputTag,
    associatorSimToReco = cms.required.InputTag,
    recoToSimScoreCut = cms.required.double,
    particleTypesSignal = cms.required.vint32,
    ignoreSuperclusterSeed = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
