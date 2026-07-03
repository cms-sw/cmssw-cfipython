import FWCore.ParameterSet.Config as cms

def PFAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('PFAnalyzer',
    puppiWeight = cms.InputTag('puppi'),
    runNumber = cms.uint32(0),
    isMiniAOD = cms.bool(True),
    pfCandidates = cms.InputTag('particleFlow'),
    pfJetCollection = cms.InputTag('ak4PFJets'),
    TriggerResultsLabel = cms.InputTag('TriggerResults', '', 'HLT'),
    eventSelection = cms.string('nocut'),
    TriggerNames = cms.vstring(),
    PVCollection = cms.InputTag('offlinePrimaryVertices'),
    pfAnalysis = cms.PSet(
      pfNames = cms.vstring(
        'allPFC',
        'neutralHadPFC',
        'chargedHadPFC',
        'electronPFC',
        'muonPFC',
        'gammaPFC',
        'hadHFPFC',
        'emHFPFC'
      ),
      observables = cms.vstring(),
      eventObservables = cms.vstring(),
      pfInJetObservables = cms.vstring(),
      NPVBins = cms.vdouble(),
      cutList = cms.vstring(),
      binList2D = cms.vstring(),
      jetCutList = cms.vstring()
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
