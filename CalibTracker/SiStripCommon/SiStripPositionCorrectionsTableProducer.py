import FWCore.ParameterSet.Config as cms

def SiStripPositionCorrectionsTableProducer(**kwargs):
  mod = cms.EDProducer('SiStripPositionCorrectionsTableProducer',
    name = cms.string('cluster'),
    doc = cms.string('On-track cluster properties for Lorentz angle and backplane correction measurement'),
    extension = cms.bool(False),
    Tracks = cms.InputTag('generalTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
