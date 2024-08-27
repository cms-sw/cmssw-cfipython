import FWCore.ParameterSet.Config as cms

def L6SLBCorrectorProducer(**kwargs):
  mod = cms.EDProducer('L6SLBCorrectorProducer',
    level = cms.required.string,
    algorithm = cms.required.string,
    srcBTagInfoElectron = cms.required.InputTag,
    srcBTagInfoMuon = cms.required.InputTag,
    addMuonToJet = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
