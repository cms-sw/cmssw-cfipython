import FWCore.ParameterSet.Config as cms

def PFLinker(*args, **kwargs):
  mod = cms.EDProducer('PFLinker',
    PFCandidate = cms.VInputTag('particleFlow'),
    GsfElectrons = cms.InputTag('gedGsfElectrons'),
    Photons = cms.InputTag('gedPhotons'),
    Muons = cms.InputTag('muons', 'muons1stStep2muonsMap'),
    ProducePFCandidates = cms.bool(True),
    FillMuonRefs = cms.bool(True),
    OutputPF = cms.string(''),
    ValueMapElectrons = cms.string('electrons'),
    ValueMapPhotons = cms.string('photons'),
    ValueMapMerged = cms.string('all'),
    forceElectronsInHGCAL = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
