import FWCore.ParameterSet.Config as cms

def RecoTrackTrackingParticleAssociationFlatTableProducer(*args, **kwargs):
  mod = cms.EDProducer('RecoTrackTrackingParticleAssociationFlatTableProducer',
    src = cms.required.InputTag,
    keySrc = cms.required.InputTag,
    valSrc = cms.required.InputTag,
    name = cms.required.string,
    doc = cms.string(''),
    linksName = cms.required.string,
    linksDoc = cms.string(''),
    scorePrecision = cms.int32(14),
    skipNonExistingSrc = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
