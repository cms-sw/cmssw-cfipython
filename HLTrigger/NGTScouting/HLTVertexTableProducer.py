import FWCore.ParameterSet.Config as cms

def HLTVertexTableProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTVertexTableProducer',
    skipNonExistingSrc = cms.bool(False),
    pvName = cms.required.string,
    pvSrc = cms.required.InputTag,
    pfSrc = cms.required.InputTag,
    goodPvCut = cms.required.string,
    dlenMin = cms.required.double,
    dlenSigMin = cms.required.double,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
