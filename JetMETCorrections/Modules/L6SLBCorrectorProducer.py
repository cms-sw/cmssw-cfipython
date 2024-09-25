import FWCore.ParameterSet.Config as cms

def L6SLBCorrectorProducer(*args, **kwargs):
  mod = cms.EDProducer('L6SLBCorrectorProducer',
    level = cms.required.string,
    algorithm = cms.required.string,
    srcBTagInfoElectron = cms.required.InputTag,
    srcBTagInfoMuon = cms.required.InputTag,
    addMuonToJet = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
