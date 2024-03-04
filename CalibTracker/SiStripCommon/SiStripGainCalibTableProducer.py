import FWCore.ParameterSet.Config as cms

def SiStripGainCalibTableProducer(**kwargs):
  mod = cms.EDProducer('SiStripGainCalibTableProducer',
    name = cms.string('cluster'),
    doc = cms.string(''),
    extension = cms.bool(False),
    Tracks = cms.InputTag('generalTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
