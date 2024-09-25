import FWCore.ParameterSet.Config as cms

def PFElectronTranslator(*args, **kwargs):
  mod = cms.EDProducer('PFElectronTranslator',
    PFCandidate = cms.InputTag('pfSelectedElectrons'),
    PFCandidateElectron = cms.InputTag('particleFlowTmp', 'electrons'),
    GSFTracks = cms.InputTag('electronGsfTracks'),
    PFBasicClusters = cms.string('pf'),
    PFPreshowerClusters = cms.string('pf'),
    PFSuperClusters = cms.string('pf'),
    ElectronMVA = cms.string('pf'),
    ElectronSC = cms.string('pf'),
    PFGsfElectron = cms.string('pf'),
    PFGsfElectronCore = cms.string('pf'),
    MVACutBlock = cms.PSet(),
    CheckStatusFlag = cms.bool(True),
    useIsolationValues = cms.bool(False),
    isolationValues = cms.PSet(
      pfSumChargedHadronPt = cms.InputTag('elPFIsoValueCharged04PFId'),
      pfSumPhotonEt = cms.InputTag('elPFIsoValueGamma04PFId'),
      pfSumNeutralHadronEt = cms.InputTag('elPFIsoValueNeutral04PFId'),
      pfSumPUPt = cms.InputTag('elPFIsoValuePU04PFId')
    ),
    emptyIsOk = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
