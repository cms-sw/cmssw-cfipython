import FWCore.ParameterSet.Config as cms

def TestIdealGeometryESProducer(**kwargs):
  mod = cms.EDAnalyzer('TestIdealGeometryESProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
