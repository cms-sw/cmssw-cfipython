import FWCore.ParameterSet.Config as cms

def GEMEffByGEMCSCSegmentClient(*args, **kwargs):
  mod = cms.EDProducer('GEMEffByGEMCSCSegmentClient',
    confidenceLevel = cms.untracked.double(0.683),
    logCategory = cms.untracked.string('GEMEffByGEMCSCSegmentClient'),
    folder = cms.untracked.string('GEM/Efficiency/GEMCSCSegment'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
