import FWCore.ParameterSet.Config as cms

def Phase1L1TJetProducer(**kwargs):
  mod = cms.EDProducer('Phase1L1TJetProducer',
    inputCollectionTag = cms.InputTag('l1pfCandidates', 'Puppi'),
    etaBinning = cms.required.vdouble,
    nBinsPhi = cms.uint32(72),
    phiLow = cms.double(-3.1415926535897931),
    phiUp = cms.double(3.1415926535897931),
    jetIEtaSize = cms.uint32(7),
    jetIPhiSize = cms.uint32(7),
    trimmedGrid = cms.bool(False),
    seedPtThreshold = cms.double(5),
    ptlsb = cms.double(0.25),
    philsb = cms.double(0.0043633231),
    etalsb = cms.double(0.0043633231),
    puSubtraction = cms.bool(False),
    outputCollectionName = cms.string('UncalibratedPhase1L1TJetFromPfCandidates'),
    vetoZeroPt = cms.bool(True),
    etaRegions = cms.required.vdouble,
    phiRegions = cms.required.vdouble,
    maxInputsPerRegion = cms.uint32(18),
    sinPhi = cms.required.vdouble,
    cosPhi = cms.required.vdouble,
    metAbsEtaCut = cms.double(3),
    metHFAbsEtaCut = cms.double(5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod