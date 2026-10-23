import FWCore.ParameterSet.Config as cms

def ElasticPlotDQMSource(*args, **kwargs):
  mod = cms.EDProducer('ElasticPlotDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
