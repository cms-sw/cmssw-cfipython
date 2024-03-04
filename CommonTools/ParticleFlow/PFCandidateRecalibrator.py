import FWCore.ParameterSet.Config as cms

def PFCandidateRecalibrator(**kwargs):
  mod = cms.EDProducer('PFCandidateRecalibrator',
    pfcandidates = cms.InputTag('particleFlow'),
    shortFibreThr = cms.double(1.4),
    longFibreThr = cms.double(1.4),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
