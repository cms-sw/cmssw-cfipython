import FWCore.ParameterSet.Config as cms

def SiStripPositionCorrectionsTableProducer(*args, **kwargs):
  mod = cms.EDProducer('SiStripPositionCorrectionsTableProducer',
    name = cms.string('cluster'),
    doc = cms.string('On-track cluster properties for Lorentz angle and backplane correction measurement'),
    extension = cms.bool(False),
    Tracks = cms.InputTag('generalTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
