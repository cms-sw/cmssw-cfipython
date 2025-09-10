import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerDemonstrator(*args, **kwargs):
  mod = cms.ESProducer('trackerTFP::ProducerDemonstrator',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
