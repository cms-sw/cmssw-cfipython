import FWCore.ParameterSet.Config as cms

def HGCalConfigurationESProducer(*args, **kwargs):
  mod = cms.ESSource('HGCalConfigurationESProducer',
    indexSource = cms.ESInputTag('', ''),
    fedjson = cms.required.FileInPath,
    modjson = cms.required.FileInPath,
    bePassthroughMode = cms.int32(-1),
    cbHeaderMarker = cms.int32(-1),
    slinkHeaderMarker = cms.int32(-1),
    econdHeaderMarker = cms.int32(-1),
    charMode = cms.int32(-1),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
