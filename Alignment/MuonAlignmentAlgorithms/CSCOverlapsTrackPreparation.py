import FWCore.ParameterSet.Config as cms

def CSCOverlapsTrackPreparation(**kwargs):
  mod = cms.EDProducer('CSCOverlapsTrackPreparation',
    src = cms.InputTag('ALCARECOMuAlBeamHaloOverlaps'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
