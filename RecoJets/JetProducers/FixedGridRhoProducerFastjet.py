import FWCore.ParameterSet.Config as cms

def FixedGridRhoProducerFastjet(*args, **kwargs):
  mod = cms.EDProducer('FixedGridRhoProducerFastjet',
    maxRapidity = cms.double(5),
    gridSpacing = cms.double(0.55),
    pfCandidatesTag = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
