import FWCore.ParameterSet.Config as cms

def SiStripGainCalibTableProducer(*args, **kwargs):
  mod = cms.EDProducer('SiStripGainCalibTableProducer',
    name = cms.string('cluster'),
    doc = cms.string(''),
    extension = cms.bool(False),
    Tracks = cms.InputTag('generalTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
