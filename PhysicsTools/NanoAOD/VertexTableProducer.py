import FWCore.ParameterSet.Config as cms

def VertexTableProducer(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
