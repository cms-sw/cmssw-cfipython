import FWCore.ParameterSet.Config as cms

def TICLPFValidation(*args, **kwargs):
  mod = cms.EDProducer('TICLPFValidation',
    folder = cms.string('HGCAL/'),
    ticlPFCandidates = cms.InputTag('pfTICL'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
