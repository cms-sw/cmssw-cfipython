import FWCore.ParameterSet.Config as cms

def HiFJRhoProducer(**kwargs):
  mod = cms.EDProducer('HiFJRhoProducer',
    jetSource = cms.InputTag('kt4PFJets'),
    nExcl = cms.int32(2),
    etaMaxExcl = cms.double(2),
    ptMinExcl = cms.double(20),
    nExcl2 = cms.int32(2),
    etaMaxExcl2 = cms.double(2),
    ptMinExcl2 = cms.double(20),
    etaRanges = cms.vdouble(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
