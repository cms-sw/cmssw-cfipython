import FWCore.ParameterSet.Config as cms

def TriggerObjectTableProducer(*args, **kwargs):
  mod = cms.EDProducer('TriggerObjectTableProducer',
    name = cms.required.string,
    src = cms.required.InputTag,
    l1EG = cms.required.InputTag,
    l1Sum = cms.required.InputTag,
    l1Jet = cms.required.InputTag,
    l1Muon = cms.required.InputTag,
    l1Tau = cms.required.InputTag,
    selections = cms.PSet(
      allowAnyLabel_ = cms.required.PSetTemplate(
        doc = cms.string(''),
        id = cms.required.int32,
        sel = cms.required.string,
        skipObjectsNotPassingQualityBits = cms.required.bool,
        qualityBits = cms.required.VPSet,
        l1seed = cms.required.string,
        l1deltaR = cms.required.double,
        l1seed_2 = cms.required.string,
        l1deltaR_2 = cms.required.double,
        l2seed = cms.required.string,
        l2deltaR = cms.required.double
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
