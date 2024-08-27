import FWCore.ParameterSet.Config as cms

def NanoAODBaseCrossCleaner(**kwargs):
  mod = cms.EDProducer('NanoAODBaseCrossCleaner',
    name = cms.required.string,
    doc = cms.required.string,
    jets = cms.required.InputTag,
    muons = cms.required.InputTag,
    electrons = cms.required.InputTag,
    lowPtElectrons = cms.required.InputTag,
    taus = cms.required.InputTag,
    photons = cms.required.InputTag,
    jetSel = cms.required.string,
    muonSel = cms.required.string,
    electronSel = cms.required.string,
    lowPtElectronSel = cms.required.string,
    tauSel = cms.required.string,
    photonSel = cms.required.string,
    jetName = cms.required.string,
    muonName = cms.required.string,
    electronName = cms.required.string,
    lowPtElectronName = cms.required.string,
    tauName = cms.required.string,
    photonName = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
