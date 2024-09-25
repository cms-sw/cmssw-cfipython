import FWCore.ParameterSet.Config as cms

def PFCandidateRecalibrator(*args, **kwargs):
  mod = cms.EDProducer('PFCandidateRecalibrator',
    pfcandidates = cms.InputTag('particleFlow'),
    shortFibreThr = cms.double(1.4),
    longFibreThr = cms.double(1.4),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
