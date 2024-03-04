import FWCore.ParameterSet.Config as cms

def GEMEffByGEMCSCSegmentClient(**kwargs):
  mod = cms.EDProducer('GEMEffByGEMCSCSegmentClient',
    confidenceLevel = cms.untracked.double(0.683),
    logCategory = cms.untracked.string('GEMEffByGEMCSCSegmentClient'),
    folder = cms.untracked.string('GEM/Efficiency/GEMCSCSegment'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
