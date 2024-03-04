import FWCore.ParameterSet.Config as cms

def TICLPFValidation(**kwargs):
  mod = cms.EDProducer('TICLPFValidation',
    folder = cms.string('HGCAL/'),
    ticlPFCandidates = cms.InputTag('pfTICL'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
