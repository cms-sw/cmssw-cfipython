import FWCore.ParameterSet.Config as cms

def CSCOverlapsTrackPreparation(*args, **kwargs):
  mod = cms.EDProducer('CSCOverlapsTrackPreparation',
    src = cms.InputTag('ALCARECOMuAlBeamHaloOverlaps'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
