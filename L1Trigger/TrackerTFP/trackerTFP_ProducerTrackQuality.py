import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerTrackQuality(*args, **kwargs):
  mod = cms.ESProducer('trackerTFP::ProducerTrackQuality',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
