import FWCore.ParameterSet.Config as cms

def AssociationMapAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('AssociationMapAnalyzer',
    inputTag1 = cms.required.InputTag,
    inputTag2 = cms.required.InputTag,
    associationMapTag1 = cms.required.InputTag,
    associationMapTag2 = cms.required.InputTag,
    associationMapTag3 = cms.required.InputTag,
    associationMapTag4 = cms.required.InputTag,
    associationMapTag5 = cms.required.InputTag,
    associationMapTag6 = cms.required.InputTag,
    associationMapTag7 = cms.required.InputTag,
    associationMapTag8 = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
