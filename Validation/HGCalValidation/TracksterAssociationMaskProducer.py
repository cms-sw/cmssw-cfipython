import FWCore.ParameterSet.Config as cms

def TracksterAssociationMaskProducer(*args, **kwargs):
  mod = cms.EDProducer('TracksterAssociationMaskProducer',
    tracksters = cms.required.InputTag,
    associatorRecoToSim = cms.required.InputTag,
    associatorSimToReco = cms.required.InputTag,
    recoToSimScoreCut = cms.required.double,
    recoToSimScoreCut_forFakes = cms.required.double,
    particleTypesSignal = cms.required.vint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
