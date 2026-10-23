import FWCore.ParameterSet.Config as cms

def VertexTableProducer(*args, **kwargs):
  mod = cms.EDProducer('VertexTableProducer',
    pvSrc = cms.required.InputTag,
    pfcSrc = cms.required.InputTag,
    goodPvCut = cms.required.string,
    svSrc = cms.required.InputTag,
    svCut = cms.required.string,
    dlenMin = cms.required.double,
    dlenSigMin = cms.required.double,
    pvName = cms.required.string,
    svName = cms.required.string,
    svDoc = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
